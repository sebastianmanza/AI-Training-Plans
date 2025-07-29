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
  let height: CGFloat
  let width: CGFloat
  let background: Color
  let accentColor: Color
  let fontSize: CGFloat
    var overlayImage : Image? = nil

  var body: some View {
    TextField("", text: $text)
          .placeholder(when: text.isEmpty) {
            ZStack {
              HStack {
                if let overlayImage = overlayImage {
                  overlayImage
                    .resizable()
                    .scaledToFit()
                    .frame(width: 20, height: 20)
                    .padding(.leading, 15)
                }
                Spacer()
              }

              // Placeholder text

              Text(prompt)
                .foregroundColor(accentColor)
                .font(.custom("MADEOkineSansPERSONALUSE-Light", size: fontSize))
            }
          }
      .multilineTextAlignment(.center)
      .foregroundColor(accentColor)
      .frame(width: width, height: height)
      .background(background)
      .clipShape(Capsule())
      .font(.custom("MADEOkineSansPERSONALUSE-Light", size: fontSize))
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
  let height: CGFloat
  let width: CGFloat
  let background: Color
  let accentColor: Color
  let fontSize: CGFloat
  var overlayImage: Image? = nil

  var body: some View {

    SecureField("", text: $text)
      .placeholder(when: text.isEmpty) {
        ZStack {
          HStack {
            if let overlayImage = overlayImage {
              overlayImage
                .resizable()
                .scaledToFit()
                .frame(width: 20, height: 20)
                .padding(.leading, 15)
            }
            Spacer()
          }

          // Placeholder text

          Text(prompt)
            .foregroundColor(accentColor)
            .font(.custom("MADEOkineSansPERSONALUSE-Light", size: fontSize))
        }
      }
      .frame(maxWidth: .infinity)
      .multilineTextAlignment(.center)
      .foregroundColor(accentColor)
      .frame(width: width, height: height)
      .background(background)
      .clipShape(Capsule())
      .font(.custom("MADEOkineSansPERSONALUSE-Light", size: fontSize))
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
    Button(action: action) {
      Text(buttonTitle)
        .frame(width: 275, height: 40)
        .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 20))  // Custom font
        .foregroundColor(.white)
        .background(color)
        .clipShape(Capsule())
    }
  }
}

/* A single arrow circular button for survey answers */
struct SurveyNextButton: View {
  let action: () -> Void
  let color: Color
  var foreground: Color = .white

  var body: some View {
    Button(action: action) {
      Image(systemName: "arrow.right")
        .font(.system(size: 35, weight: .bold))
        .foregroundColor(foreground)
        .frame(width: 60, height: 60)
        .background(color)
        .clipShape(Circle())
    }
  }
}

/* A clear button with a drop shadow, used for survey selection. Highlights with a white stroke when selected */
struct SurveySelectionButton: View {
  let title: String
  let isSelected: Bool
  let height: CGFloat
  let action: () -> Void
  private let themeColor = Color(red: 40 / 255, green: 40 / 255, blue: 40 / 255)

  var body: some View {
    Button(action: action) {
      Text(title)
        .font(.custom("MADEOkineSansPERSONALUSE-Regular", size: 20))
        .foregroundColor(.white)
        .frame(minWidth: 300, minHeight: height)
        .background(themeColor)
        .overlay(
          RoundedRectangle(cornerRadius: 20, style: .continuous)
            .stroke(isSelected ? Color.white : Color.clear, lineWidth: 2)
        )
        .clipShape(RoundedRectangle(cornerRadius: 20, style: .continuous))
    }
    .shadow(color: Color.black.opacity(0.6), radius: 60, x: 0, y: 0)
  }
}

struct CheckButton: View {
  let action: () -> Void

  var body: some View {
    Button(action: action) {
      Image(systemName: "checkmark")
        .font(.system(size: 25, weight: .bold))
        .foregroundColor(.white)
        .frame(width: 35, height: 35)
        .background(.green)
        .clipShape(RoundedRectangle(cornerRadius: 10, style: .continuous))
    }
  }
}

struct XButton: View {
  let action: () -> Void

  var body: some View {
    Button(action: action) {
      Image(systemName: "xmark")
        .font(.system(size: 25, weight: .bold))
        .foregroundColor(.white)
        .frame(width: 35, height: 35)
        .background(.red)
        .clipShape(RoundedRectangle(cornerRadius: 10, style: .continuous))
    }
  }
}

struct QuestionMarkButton: View {
  let action: () -> Void

  var body: some View {
    Button(action: action) {
      Image(systemName: "questionmark")
        .font(.system(size: 15, weight: .bold))
        .foregroundColor(.white)
        .frame(width: 25, height: 25)
        .background(.clear)
        .overlay(Circle().stroke(.white, lineWidth: 2))
        .clipShape(Circle())
    }
  }
}

struct XButtonQuestionMarkStyle: View {
  let action: () -> Void

  var body: some View {
    Button(action: action) {
      Image(systemName: "xmark")
        .font(.system(size: 15, weight: .bold))
        .foregroundColor(.white)
        .frame(width: 25, height: 25)
        .background(.clear)
        .overlay(Circle().stroke(.white, lineWidth: 2))
        .clipShape(Circle())
    }
  }
}

struct CalendarButton: View {
  let action: () -> Void

  var body: some View {
    Button(action: action) {
      Image(systemName: "calendar")
        .font(.system(size: 40, weight: .bold))
        .foregroundColor(.white)
    }
    .frame(width: 45, height: 45)
    .background(.clear)
    .clipShape(RoundedRectangle(cornerRadius: 10, style: .continuous))
  }
}

struct ProfileButton: View {
  let action: () -> Void

  var body: some View {
    Button(action: action) {
      Image(systemName: "person")
        .font(.system(size: 40, weight: .bold))
        .foregroundColor(.white)
    }
    .frame(width: 45, height: 45)
    .background(.clear)
    .clipShape(RoundedRectangle(cornerRadius: 10, style: .continuous))
  }
}
