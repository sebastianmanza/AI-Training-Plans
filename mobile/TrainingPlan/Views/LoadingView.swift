import SwiftUI

struct LoadingView: View {
  @State private var isAnimating = false

  var body: some View {
    ZStack {
      Image("loadingBackground")
        .resizable()
        .scaledToFill()
        .edgesIgnoringSafeArea(.all)
      VStack {
        Spacer()
        Image("Logo")
          .resizable()
          .scaledToFit()
          .frame(width: 120, height: 120)
          .padding(.bottom, 20)
          .shimmer(
            duration: 0.8,
            highlight: .white.opacity(1.0),
            background: .gray.opacity(0.5))

        Text("MAKE THE DAYS COUNT.")
          .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 24))
          .foregroundColor(.white)
          .padding(.bottom, 20)
          .shimmer(
            duration: 0.8,
            highlight: .white.opacity(1.0),
            background: .gray.opacity(0.5))

        Spacer()
      }
    }
  }
}
