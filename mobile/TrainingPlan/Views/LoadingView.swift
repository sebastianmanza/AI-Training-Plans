import SwiftUI

struct LoadingView: View {
  @State private var isAnimating = false

  var body: some View {
    ZStack {
      Image("loadingBackground")
        .resizable()
        .scaledToFill()
        .edgesIgnoringSafeArea(.all)
      VStack (spacing: -5) {
        Spacer()
        Image("Logo")
          .resizable()
          .scaledToFit()
          .frame(width: 80, height: 80)
          .padding(.bottom, 20)
          .shimmer(
            duration: 1.5,
            highlight: .white.opacity(1.0),
            background: .gray.opacity(0.6))

        Text("MAKE THE DAYS COUNT.")
          .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 18))
          .foregroundColor(.white)
          .padding(.bottom, 20)
          .shimmer(
            duration: 1.5,
            highlight: .white.opacity(1.0),
            background: .gray.opacity(0.6))

        Spacer()
      }
    }
  }
}
