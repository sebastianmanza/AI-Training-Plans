import SwiftUI


struct FlippableCardView: View {
  let accentColorStart: Color
  let accentColorStop: Color
  let backgroundColor: Color
  let mainTextColor: Color
  let accentTextColor: Color

  @Binding var showInfo: Bool 
  @ObservedObject var vm: HomeViewModel

  let onDidNotComplete: () -> Void
  let onCompleted: () -> Void

  let cardWidth: CGFloat
  let cardHeight: CGFloat

  var body: some View {
    ZStack {
      // Front side
      MainStimulus(
        accentColorStart: accentColorStart,
        accentColorStop: accentColorStop,
        backgroundColor: backgroundColor,
        cardWidth: cardWidth,
        cardHeight: cardHeight,
        mainTextColor: mainTextColor,
        accentTextColor: accentTextColor,
        vm: vm
      )
      .opacity(showInfo ? 0 : 1)
      .overlay(
        HStack {
            Spacer()
            XButton {
                withAnimation(.spring()) { onDidNotComplete() }
            }
            CheckButton {
                withAnimation(.spring()) { onCompleted() }
            }
        }
        .padding(.bottom, 20)
        .padding(.trailing, 50),
        alignment: .bottomTrailing
      )
      .allowsHitTesting(!showInfo)
      .opacity(showInfo ? 0 : 1)

      // Back side
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
      .padding(.trailing, 45),
      alignment: .topTrailing
    )
    .frame(width: cardWidth, height: cardHeight)
    .clipShape(RoundedRectangle(cornerRadius: 20, style: .continuous))
    .shadow(color: .black.opacity(0.6), radius: 60, x: 0, y: 0)
  }
}
