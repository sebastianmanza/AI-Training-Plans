import SwiftUI

struct FlippableCardView: View {

  @Binding var showInfo: Bool
  @ObservedObject var vm: HomeViewModel

  let onDidNotComplete: () -> Void
  let onCompleted: () -> Void

  let cardWidth: CGFloat
  let cardHeight: CGFloat

  var body: some View {
    ZStack {
      // background
      BlurEffect(style: .regular)
        .overlay(
          // foreground
          VStack(spacing: 25) {
            if let data = vm.homeData {
              Text(data.day.uppercased())
                .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 24))
                .foregroundColor(.white)
                .multilineTextAlignment(.center)

              Rectangle()
                .fill(.white)
                .frame(width: cardWidth * 0.8, height: 1.5)
                .padding(.bottom, 20)

              Text("\(data.mileage.formattedMileage) MILES")
                .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 48))
                .foregroundColor(.white)
                .multilineTextAlignment(.center)

              VStack(alignment: .leading, spacing: 20) {
                HStack(spacing: 20) {
                  Text("PACE:")
                    .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 20))
                    .foregroundColor(.white)

                  Text(data.pace)
                    .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 20))
                    .foregroundColor(.white)
                }
                HStack(spacing: 20) {
                  Text("WORKOUT:")
                    .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 20))
                    .foregroundColor(.white)

                  Text(data.stimuli.uppercased())
                    .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 20))
                    .foregroundColor(.white)
                }

                HStack(spacing: 20) {
                  Text("GOAL RPE:")
                    .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 20))
                    .foregroundColor(.white)

                  Text(data.goalRPE)
                    .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 20))
                    .foregroundColor(.white)
                }
              }

              HStack(spacing: 15) {
                Spacer()
                XButton(action: onDidNotComplete)
                CheckButton(action: onCompleted)
                  .padding(.trailing, 25)
              }
            } else {
              ProgressView()
                .foregroundColor(.white)
            }

          }
          .opacity(showInfo ? 0 : 1))
          .allowsHitTesting(!showInfo)

      VStack {
        Text("Info")
          .font(.headline)
          .foregroundColor(.white)
        Text("Details blah blah blah")
          .multilineTextAlignment(.center)
          .padding()
          .foregroundColor(.white)
      }
      .rotation3DEffect(
        .degrees(180),
        axis: (x: 0, y: 1, z: 0)
      )

      .opacity(showInfo ? 1 : 0)
      .allowsHitTesting(showInfo)
    }
    .rotation3DEffect(
      .degrees(showInfo ? 180 : 0),
      axis: (x: 0, y: 1, z: 0),
      perspective: 0.5
    )
    .overlay(
      Group {
        if !showInfo {
          QuestionMarkButton {
            withAnimation(.spring()) { showInfo.toggle() }
          }
        } else {
          XButtonQuestionMarkStyle {
            withAnimation(.spring()) { showInfo.toggle() }
          }
        }
      }
      .padding(.top, 15)
      .padding(.trailing, 15),
      alignment: .topTrailing
    )
    .frame(width: cardWidth, height: cardHeight)
    .clipShape(RoundedRectangle(cornerRadius: 20, style: .continuous))
    .shadow(color: .black.opacity(0.6), radius: 60, x: 0, y: 0)

  }
}
