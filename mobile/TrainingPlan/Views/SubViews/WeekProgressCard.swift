import SwiftUI

struct WeekProgressCard: View {
  let textMainColor: Color
  let textAccentColor: Color
  let accentColor: Color
  @ObservedObject var vm: HomeViewModel

  var body: some View {
    ZStack {
      /* Background */
      RoundedRectangle(cornerRadius: 20)
        .fill(Color(red: 40 / 255, green: 40 / 255, blue: 40 / 255))

      /* Foreground */
      VStack(spacing: 5) {
        if let data = vm.homeData {
          HStack {
            Text("Week 1")
              .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 20))
              .foregroundColor(textMainColor)
            
            Spacer()

            Text("40 miles")
              .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 20))
              .foregroundColor(textMainColor)
          }
          .padding(.bottom, 20)
          HStack {
            Text("Progress")
              .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 16))
              .foregroundColor(textAccentColor)

            Spacer()
            Text("Week stimuli: build")
              .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 16))
              .foregroundColor(textAccentColor)
          }
          CompletionBar(
            background: .white,
            fill: accentColor,
            width: 275,
            height: 13,
            percentComplete: 0.25
          )
        } else {
          ProgressView()
            .foregroundColor(.white)
        }
      }
      .padding(.horizontal, 50)
    }
  }
}
