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
          .padding(.vertical, 20)

          HStack {
            Text("Progress")
              .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 16))
              .foregroundColor(textAccentColor)

            Spacer()
            Text("Week stimuli: build")
              .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 16))
              .foregroundColor(textAccentColor)
          }
          GeometryReader { geo in
            CompletionBar(
              background: .white,
              fill: accentColor,
              width: geo.size.width,
              height: 13,
              percentComplete: 0.2
            )
          }
        } else {
          ProgressView()
            .foregroundColor(.white)
        }
      }
      .padding(.horizontal, 50)
    }
  }
}
