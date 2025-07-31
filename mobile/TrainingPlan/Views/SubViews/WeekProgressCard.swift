import SwiftUI

struct WeekProgressPager: View {
  @ObservedObject var vm: HomeViewModel
  @State private var selectedIndex: Int = 0

  var body: some View {
    if let data = vm.homeData {
      TabView(selection: $selectedIndex) {
        ForEach(0..<data.weeknum.count, id: \.self) { idx in
          WeekProgressCard(
            textMainColor: Color.headertext,
            textAccentColor: Color.bodytext,
            accentColor: Color.accent,
            index: idx,
            vm: vm
          )
          .tag(idx)
        }
      }
      .tabViewStyle(PageTabViewStyle(indexDisplayMode: .never))
      .overlay(
        PageIndicatorStyle(
          selectedIndex: $selectedIndex,
          selectedColor: .accent,
          unselectedColor: .headertext,
          dotSize: 10,
          numDots: 3,
          dotSpacing: 10
        )
        .padding(.bottom, 5),
        alignment: .bottom
      )
    } else {
      WeekProgressCard(
        textMainColor: Color.headertext,
        textAccentColor: Color.bodytext,
        accentColor: Color.accent,
        index: 0,
        vm: vm
      )
      .tag(0)
    }

  }
}

struct WeekProgressCard: View {
  let textMainColor: Color
  let textAccentColor: Color
  let accentColor: Color
  var index: Int
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
            Text("Week \(data.weeknum[index])")
              .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 20))
              .foregroundColor(textMainColor)

            Spacer()

            Text("\(data.weekmileage[index].formattedMileage) miles")
              .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 20))
              .foregroundColor(textMainColor)
          }
          .padding(.top, 20)
          .padding(.bottom, 10)

          HStack {
            Text("Progress")
              .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 16))
              .foregroundColor(textAccentColor)

            Spacer()
            Text("Week stimuli: \(data.weekstimuli[index])")
              .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 16))
              .foregroundColor(textAccentColor)
          }
          GeometryReader { geo in
            CompletionBar(
              background: .white,
              fill: accentColor,
              width: geo.size.width,
              height: 13,
              percentComplete: CGFloat(data.weekpctcomplete[index])
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
