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
/// `URLSession` instance under the hood. The base URL is resolved from the
/// `API_BASE_URL` environment variable or, if unset, an `APIConfig.plist`
/// file in the application bundle.
final class APIClient {
  static let shared = APIClient()

  /// Resolve the base URL from an environment variable or configuration file.
  private let baseURL: URL = {
    if let env = ProcessInfo.processInfo.environment["API_BASE_URL"],
       let urlObj = URL(string: env) {
      return urlObj
    }

    if
      let url = Bundle.main.url(forResource: "APIConfig", withExtension: "plist"),
      let data = try? Data(contentsOf: url),
      let dict = try? PropertyListSerialization.propertyList(from: data, options: [], format: nil) as? [String: Any],
      let base = dict["API_BASE_URL"] as? String,
      let urlObj = URL(string: base)
    {
      return urlObj
    }

    preconditionFailure("API_BASE_URL not configured. Set API_BASE_URL env var or provide APIConfig.plist")
  }()

  private let session: URLSession

  private init(session: URLSession = .shared) {
    self.session = session

    #if DEBUG
    let isDebug = true
    #else
    let isDebug = false
    #endif

    let allowHTTPEnv = ProcessInfo.processInfo.environment["API_ALLOW_HTTP"]
    let allowHTTP = allowHTTPEnv != nil &&
      allowHTTPEnv!.lowercased() != "false" &&
      allowHTTPEnv != "0"

    precondition(baseURL.scheme?.lowercased() == "https" || isDebug || allowHTTP,
                 "APIClient requires an HTTPS base URL. Set API_ALLOW_HTTP=1 to allow HTTP.")
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

  /// Retrieves the Home page data for the authenticated user.
  func fetchHomeData() async throws -> HomeData {
    let data = try await sendRequest("home/data")
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

