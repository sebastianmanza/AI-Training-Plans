import SwiftUI

struct UpcomingCard: View {
  let accentColorStart: Color
  let accentColorStop: Color
  let backgroundColor: Color
  let mainTextColor: Color
  let accentTextColor: Color
  @ObservedObject var vm: HomeViewModel

  var body: some View {
    ZStack {
      RoundedRectangle(cornerRadius: 20)
        .fill(
          LinearGradient(
            gradient: Gradient(colors: [accentColorStart, accentColorStop]),
            startPoint: .top,
            endPoint: .bottom
          )
        )

      Rectangle()
        .fill(backgroundColor)
        .frame(maxWidth: .infinity)
        .padding(.horizontal, 25)

      /* Foreground */
      VStack(alignment: .leading, spacing: 10) {
        if let data = vm.homeData {
          Group {
            Text(data.upcoming)
              .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 20))
              .foregroundColor(mainTextColor)

            HStack {
              Text("\(data.upcomingmileage.formattedMileage) miles")
                .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 16))
                .foregroundColor(accentTextColor)

              Spacer()

              Text("\(data.upcomingtime)")
                .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 16))
                .foregroundColor(accentTextColor)
            }
          }
          .padding(.horizontal, 50)
        } else {
          ProgressView()
            .foregroundColor(.white)
        }
      }
    }
  }
}
