import Foundation

struct SignupIn: Codable {
  let email: String
  let username: String
  let password: String
}

struct LoginIn: Codable {
  let username: String
  let password: String
}

struct RefreshIn: Codable {
  let refresh_token: String
}

struct AuthOut: Codable {
  let user_id: Int?
  let error_code: Int?
  let access_token: String?
  let refresh_token: String?
}
