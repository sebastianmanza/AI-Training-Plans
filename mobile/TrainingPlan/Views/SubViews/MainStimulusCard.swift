import SwiftUI

struct MainStimulus: View {
  let accentColorStart: Color
  let accentColorStop: Color
  let backgroundColor: Color
  let cardWidth: CGFloat
  let cardHeight: CGFloat
  let mainTextColor: Color
  let accentTextColor: Color
  @ObservedObject var vm: HomeViewModel

  var body: some View {
    ZStack {
      /*Card background*/
      RoundedRectangle(cornerRadius: 20)
        .fill(
          LinearGradient(
            gradient: Gradient(colors: [accentColorStart, accentColorStop]),
            startPoint: .top,
            endPoint: .bottom
          )
        )
        .frame(width: cardWidth, height: cardHeight)

      /*Card background layer 2*/
      Rectangle()
        .fill(backgroundColor)
        .frame(width: cardWidth - 50, height: cardHeight)

      /*Card foreground*/
      VStack(alignment: .leading, spacing: 5) {
        if let data = vm.homeData {
          Spacer()
          Text(data.stimuli)
            .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 36))
            .foregroundColor(mainTextColor)

          Text("\(data.mileage.formattedMileage) miles")
            .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 32))
            .foregroundColor(accentTextColor)

          Spacer()

          Text("Pace: \(data.pace)\nGoal RPE: \(data.goalRPE)")
            .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 24))
            .foregroundColor(accentTextColor)

          Spacer()

          Text(data.time)
            .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 16))
            .foregroundColor(accentTextColor)
            .padding(.bottom, 20)
        } else {
          ProgressView()
            .foregroundColor(.white)
        }
      }
    }
  }
}
