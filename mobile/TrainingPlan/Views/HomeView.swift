import SwiftUI

extension Float {
  var formattedMileage: String {
    truncatingRemainder(dividingBy: 1) == 0
      ? String(format: "%.0f", self)
      : String(format: "%.1f", self)
  }
}

struct HomeView: View {
  @EnvironmentObject private var session: Session
  @StateObject private var vm = HomeViewModel()

  /* The current options for clickable objects */
  var onDidNotComplete: () -> Void
  var onCalendarTapped: () -> Void
  var onProfileTapped: () -> Void
  var onDebugger: () -> Void

  @State private var showInfoOnInfoTapped = false
  @State private var showPostRunSurvey = false
  @State private var currentRPE: Double = 5.0

  var body: some View {
    NavigationStack {
      GeometryReader { geo in

        ZStack {
          /* Base background color */
          Color(red: 23 / 255, green: 23 / 255, blue: 23 / 255)
            .ignoresSafeArea()

          /*Navigation bar with buttons */

          /* Foreground, several different cards */
          VStack(spacing: 20) {
            Spacer()

            // todays card
            FlippableCardView(
              accentColorStart: Color(red: 242 / 255, green: 255 / 255, blue: 0 / 255),
              accentColorStop: Color(red: 95 / 255, green: 255 / 255, blue: 204 / 255),
              backgroundColor: Color(red: 40 / 255, green: 40 / 255, blue: 40 / 255),
              mainTextColor: .white,
              accentTextColor: Color(red: 159 / 255, green: 159 / 255, blue: 159 / 255),
              showInfo: $showInfoOnInfoTapped,
              vm: vm,
              onDidNotComplete: onDidNotComplete,
              onCompleted: { showPostRunSurvey = true },
              cardWidth: geo.size.width * 0.9,
              cardHeight: geo.size.height * 0.45
            )
            .opacity(showPostRunSurvey ? 0 : 1)

            // upcoming card
            UpcomingCard(
              accentColorStart: Color(red: 255 / 255, green: 186 / 255, blue: 95 / 255),
              accentColorStop: Color(red: 255 / 255, green: 0 / 255, blue: 0 / 255),
              backgroundColor: Color(red: 40 / 255, green: 40 / 255, blue: 40 / 255),
              viewWidth: geo.size.width * 0.9,
              viewHeight: geo.size.height * 0.12,
              mainTextColor: .white,
              accentTextColor: Color(red: 159 / 255, green: 159 / 255, blue: 159 / 255),
              vm: vm
            )
            Spacer()
          }
          .onAppear { Task { await vm.load(session: session) } }
          .padding(.bottom, 50)
          .ignoresSafeArea()
        }
        .sheet(isPresented: $showPostRunSurvey) {
          PostRunSurvey(rpeval: $currentRPE)
            .presentationDetents([.fraction(0.6)])
            .presentationDragIndicator(.visible)
            .presentationCornerRadius(40)
        }
      }
    }
    .toolbarBackground(Color(red: 40 / 255, green: 40 / 255, blue: 40 / 255), for: .navigationBar)
    .toolbarBackground(.visible, for: .navigationBar)
    .toolbarBackground(Color(red: 40 / 255, green: 40 / 255, blue: 40 / 255), for: .bottomBar)
    .toolbarBackground(.visible, for: .bottomBar)
    .toolbar {
      ToolbarItem(placement: .navigationBarLeading) {
        HStack(spacing: 12) {
          Image("Logo")
            .resizable()
            .scaledToFit()
            .frame(width: 30, height: 30)
          Text("ENDORPHIN")
            .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 15))
        }
      }
      ToolbarItem(placement: .navigationBarTrailing) {
        Button(action: onDebugger) {
          Image(systemName: "gearshape")
            .font(.system(size: 20))
        }
      }

      ToolbarItem(placement: .bottomBar) {
        HStack {
          Button(action: onDebugger) {
            Image(systemName: "ladybug")
          }
          Spacer()
          Button(action: onDebugger) {
            Image(systemName: "house")
              .foregroundColor(.white)
              .font(.system(size: 20))
          }
          Spacer()
          Button(action: onCalendarTapped) {
            Image(systemName: "calendar")
              .foregroundColor(.white)
              .font(.system(size: 20))
          }
          Spacer()
          Button(action: onProfileTapped) {
            Image(systemName: "person.crop.circle")
              .foregroundColor(.white)
              .font(.system(size: 20))
          }
        }
        .frame(maxWidth: .infinity)
      }
    }
  }
}
