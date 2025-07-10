import Foundation

enum APIError: Error {
  case badURL
  case network(Error)
  case http(Int, Data)
  case jsonDecoding(Error)
}

class APIClient {
  static let baseURL = "http://10.161.117.159:8000"

  /// Sends the survey and returns the raw JSON as a dictionary.
  static func submitPrelim(_ survey: SurveyIn) async throws -> [String: Any] {
    guard let url = URL(string: "\(baseURL)/survey/prelim") else {
      throw APIError.badURL
    }
    var req = URLRequest(url: url)
    req.httpMethod = "POST"
    req.setValue("application/json", forHTTPHeaderField: "Content-Type")
    req.httpBody = try JSONEncoder().encode(survey)

    let (data, resp): (Data, URLResponse)
    do {
      (data, resp) = try await URLSession.shared.data(for: req)
    } catch {
      throw APIError.network(error)
    }
    guard let http = resp as? HTTPURLResponse else {
      throw APIError.http(-1, data)
    }
    guard 200..<300 ~= http.statusCode else {
      throw APIError.http(http.statusCode, data)
    }
    // parse into [String:Any]
    do {
      let obj = try JSONSerialization.jsonObject(with: data)
      guard let dict = obj as? [String: Any] else {
        return [:]
      }
      return dict
    } catch {
      throw APIError.jsonDecoding(error)
    }
  }

  static func fetchHomeData() async throws -> HomeData {
    guard let url = URL(string: "\(baseURL)/home/data") else {
      throw APIError.badURL
    }
    let (data, resp) = try await URLSession.shared.data(from: url)
    guard let http = resp as? HTTPURLResponse, 200..<300 ~= http.statusCode else {
      throw APIError.http((resp as? HTTPURLResponse)?.statusCode ?? -1, data)
    }
    return try JSONDecoder().decode(HomeData.self, from: data)
  }

  static func signup(_ payload: SignupIn) async throws -> AuthOut {
    guard let url = URL(string: "\(baseURL)/auth/signup") else {
      throw APIError.badURL
    }
    var req = URLRequest(url: url)
    req.httpMethod = "POST"
    req.setValue("application/json", forHTTPHeaderField: "Content-Type")
    req.httpBody = try JSONEncoder().encode(payload)

    let (data, resp) = try await URLSession.shared.data(for: req)
    guard let http = resp as? HTTPURLResponse, 200..<300 ~= http.statusCode else {
      throw APIError.http((resp as? HTTPURLResponse)?.statusCode ?? -1, data)
    }
    return try JSONDecoder().decode(AuthOut.self, from: data)
  }

    static func login(_ payload: LoginIn) async throws -> AuthOut {
    guard let url = URL(string: "\(baseURL)/auth/login") else {
      throw APIError.badURL
    }
    var req = URLRequest(url: url)
    req.httpMethod = "POST"
    req.setValue("application/json", forHTTPHeaderField: "Content-Type")
    req.httpBody = try JSONEncoder().encode(payload)

    let (data, resp) = try await URLSession.shared.data(for: req)
    guard let http = resp as? HTTPURLResponse, 200..<300 ~= http.statusCode else {
      throw APIError.http((resp as? HTTPURLResponse)?.statusCode ?? -1, data)
    }
    return try JSONDecoder().decode(AuthOut.self, from: data)
  }
}
