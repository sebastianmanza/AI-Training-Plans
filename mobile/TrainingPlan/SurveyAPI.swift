import Foundation

enum APIError: Error {
  case badURL
  case network(Error)
  case http(Int, Data)
  case jsonDecoding(Error)
}

class SurveyAPI {
  static let baseURL = "http://YOUR_BACKEND_IP:8000"
  
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
}