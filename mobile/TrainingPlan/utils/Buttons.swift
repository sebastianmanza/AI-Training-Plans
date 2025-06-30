import SwiftUI

/* A view modifier that adds a placeholder to a view when a condition is met.
 This is useful for text fields or other input views where you want to show a hint
 when the input is empty.
 */
extension View {
    func placeholder<Content: View>(
        when shouldShow: Bool,
        alignment: Alignment = .center,
        @ViewBuilder placeholder: () -> Content
    ) -> some View {
        ZStack(alignment: alignment) {
            if shouldShow {
                placeholder()
            }
            self
        }
    }
}

/* A capsule-shaped text field that shows a placeholder when empty.
 This is used for user input fields like email, username, etc.
 */
struct CapsuleTextField: View {
    var prompt: String
    @Binding var text: String
    
    var body: some View {
        TextField("", text: $text)
            .placeholder(when: text.isEmpty) {
                Text(prompt)
                    .foregroundColor(.white)
                    .font(.custom("MADEOkineSansPERSONALUSE-Light", size: 16))
            }
            .multilineTextAlignment(.center)
            .foregroundColor(.white)
            .frame(width: 275, height: 55)
            .background(Color(red: 209/255, green: 209/255, blue: 209/255))
            .clipShape(Capsule())
            .font(.custom("MADEOkineSansPERSONALUSE-Light", size: 16))
            .autocapitalization(.none)
            .disableAutocorrection(true)
    }
}

/* A capsule-shaped password field that shows a placeholder when empty.
 This is used for user input fields like passwords.
 */
struct CapsulePasswordField: View {
    var prompt: String
    @Binding var text: String
    
    var body: some View {
        SecureField("", text: $text)
            .placeholder(when: text.isEmpty) {
                Text(prompt)
                    .foregroundColor(.white)
                    .font(.custom("MADEOkineSansPERSONALUSE-Light", size: 16))
            }
            .multilineTextAlignment(.center)
            .foregroundColor(.white)
            .frame(width: 275, height: 55)
            .background(Color(red: 209/255, green: 209/255, blue: 209/255))
            .clipShape(Capsule())
            .font(.custom("MADEOkineSansPERSONALUSE-Light", size: 16))
            .autocapitalization(.none)
            .disableAutocorrection(true)
    }
}

/* A wide button that is used for log in and signup*/ 
//TODO: Make this dynamic
struct LogInButton: View {
    let buttonTitle: String
    let action: () -> Void
    let color: Color

    var body: some View {
        Button(buttonTitle, action: action)
            .frame(width: 275, height: 40)
            .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 20)) // Custom font
            .foregroundColor(.white) // Text color
            .background(color) // Background color
            .clipShape(Capsule()) // Capsule shape
    }
}

/* A single arrow circular button for survey answers */
struct SurveyButton: View {
    let action: () -> Void
    let color: Color

    var body: some View {
        Button(action: action) {
            Image(systemName: "arrow.right")
            .font(.system(size: 35, weight: .bold))
            .foregroundColor(.white)
        }
            .frame(width: 60, height: 60)
            .background(color)
            .clipShape(Circle())
    }
}
