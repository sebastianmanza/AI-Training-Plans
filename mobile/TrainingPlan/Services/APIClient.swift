import Foundation

enum APIError: Error {
  case badURL
  case network(Error)
  case http(Int, Data)
  case jsonDecoding(Error)
}

/// `APIClient` centralizes all network communication with the backend.
///
/// The client exposes async functions for each API call and uses a single
/// `URLSession` instance under the hood. The base URL is resolved from an
/// `APIConfig.plist` file in the application bundle, falling back to the
/// `API_BASE_URL` environment variable and finally a build-specific default.
final class APIClient {
  static let shared = APIClient()

  /// Resolve the base URL from a configuration file or environment variable.
  private let baseURL: URL = {
    if
      let url = Bundle.main.url(forResource: "APIConfig", withExtension: "plist"),
      let data = try? Data(contentsOf: url),
      let dict = try? PropertyListSerialization.propertyList(from: data, options: [], format: nil) as? [String: Any],
      let base = dict["API_BASE_URL"] as? String,
      let urlObj = URL(string: base)
    {
      return urlObj
    }

    if let env = ProcessInfo.processInfo.environment["API_BASE_URL"],
       let urlObj = URL(string: env) {
      return urlObj
    }

    #if DEBUG
    return URL(string: "http://localhost:8000")!
    #else
    return URL(string: "https://localhost:8000")!
    #endif
  }()

  private let session: URLSession

  private init(session: URLSession = .shared) {
    self.session = session
#if !DEBUG
    precondition(baseURL.scheme?.lowercased() == "https",
                 "APIClient requires an HTTPS base URL in release builds.")
#endif
  }

  /// Generic request helper used by the public API methods below.
  private func sendRequest(
    _ path: String,
    method: String = "GET",
    body: Data? = nil,
    queryItems: [URLQueryItem] = []
  ) async throws -> Data {
    var components = URLComponents(url: baseURL.appendingPathComponent(path), resolvingAgainstBaseURL: false)
    components?.queryItems = queryItems.isEmpty ? nil : queryItems

    guard let url = components?.url else { throw APIError.badURL }

    var req = URLRequest(url: url)
    req.httpMethod = method
    if let body = body {
      req.setValue("application/json", forHTTPHeaderField: "Content-Type")
      req.httpBody = body
    }

    do {
      let (data, resp) = try await session.data(for: req)
      guard let http = resp as? HTTPURLResponse else { throw APIError.http(-1, data) }
      guard 200..<300 ~= http.statusCode else { throw APIError.http(http.statusCode, data) }
      return data
    } catch {
      throw APIError.network(error)
    }
  }

  /// Sends the survey and returns the raw JSON as a dictionary.
  func submitPrelim(_ survey: SurveyIn) async throws -> [String: Any] {
    let data = try await sendRequest(
      "survey/prelim",
      method: "POST",
      body: try JSONEncoder().encode(survey)
    )

    do {
      let obj = try JSONSerialization.jsonObject(with: data)
      return obj as? [String: Any] ?? [:]
    } catch {
      throw APIError.jsonDecoding(error)
    }
  }

  /// Retrieves the Home page data for the given session.
  func fetchHomeData(session: Session) async throws -> HomeData {
    guard let userID = session.userID else {
      throw APIError.http(-1, Data("No userID in session".utf8))
    }

    let data = try await sendRequest(
      "home/data",
      queryItems: [URLQueryItem(name: "user_id", value: String(userID))]
    )
    return try JSONDecoder().decode(HomeData.self, from: data)
  }

  func signup(_ payload: SignupIn) async throws -> AuthOut {
    let data = try await sendRequest(
      "auth/signup",
      method: "POST",
      body: try JSONEncoder().encode(payload)
    )
    return try JSONDecoder().decode(AuthOut.self, from: data)
  }

  func login(_ payload: LoginIn) async throws -> AuthOut {
    let data = try await sendRequest(
      "auth/login",
      method: "POST",
      body: try JSONEncoder().encode(payload)
    )
    return try JSONDecoder().decode(AuthOut.self, from: data)
  }
}

