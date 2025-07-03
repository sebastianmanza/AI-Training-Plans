import SwiftUI
import UIKit

struct HomeView: View {

  /* The current options for clickable objects */
  var onCompleted: () -> Void
  var onDidNotComplete: () -> Void
  var onQuestionMark: () -> Void
  var onCalendarTapped: () -> Void
  var onProfileTapped: () -> Void

  var body: some View {
    GeometryReader { geo in

      /* Vertically stack all the different layers (background and foreground)
       * The background is a ZStack with a gradient and a logo
       * The foreground is a Zstack with the card and buttons
       */
      ZStack {

        /* Background */
        ZStack {
          Color(red: 40 / 255, green: 40 / 255, blue: 40 / 255)
            .ignoresSafeArea()

          /* Gradient: needs to be changed so the colors aren't hard coded */
          LinearGradient(
            gradient: Gradient(stops: [
              .init(color: Color(red: 0 / 255, green: 64 / 255, blue: 255 / 255), location: 0.0),
              .init(
                color: Color(red: 153 / 255, green: 153 / 255, blue: 153 / 255).opacity(0.2),
                location: 0.40),
              .init(
                color: Color(red: 153 / 255, green: 153 / 255, blue: 153 / 255).opacity(0),
                location: 0.6),
            ]),
            startPoint: .top,
            endPoint: .bottom
          )
          .ignoresSafeArea()
        }
        .overlay(
          /* Background logo */
          Image("Logo")
            .resizable()
            .scaledToFit()
            .opacity(0.1)
            .ignoresSafeArea(.all),

          alignment: .top
        )  // background

        /* Foreground, several different cards */
        VStack(spacing: 20) {
          Spacer()

          // todays card
          ZStack {
            // background
            BlurEffect(style: .regular)
              .frame(width: geo.size.width * 0.8, height: geo.size.height * 0.55)
              .clipShape(RoundedRectangle(cornerRadius: 20, style: .continuous))
              .shadow(color: .black.opacity(0.6), radius: 60, x: 0, y: 0)
              .overlay(
                QuestionMarkButton(action: onQuestionMark)
                  .padding(.top, 15)
                  .padding(.trailing, 15),

                alignment: .topTrailing
              )
              .overlay(
                // foreground
                VStack(spacing: 25) {
                  Text("MONDAY")
                    .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 24))
                    .foregroundColor(.white)
                    .multilineTextAlignment(.center)

                  Rectangle()
                    .fill(.white)
                    .frame(width: geo.size.width * 0.65, height: 1.5)
                    .padding(.bottom, 20)

                  Text("7 MILES")
                    .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 48))
                    .foregroundColor(.white)
                    .multilineTextAlignment(.center)

                  VStack(alignment: .leading, spacing: 20) {
                    HStack(spacing: 20) {
                      Text("PACE:")
                        .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 20))
                        .foregroundColor(.white)

                      Text("7:00-7:30")
                        .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 20))
                        .foregroundColor(.white)
                    }
                    HStack(spacing: 20) {
                      Text("STIMULI:")
                        .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 20))
                        .foregroundColor(.white)

                      Text("BASE:")
                        .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 20))
                        .foregroundColor(.white)
                    }

                    HStack(spacing: 20) {
                      Text("GOAL RPE")
                        .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 20))
                        .foregroundColor(.white)

                      Text("5/10")
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
                })

          }
          BlurEffect(style: .regular)
            .frame(width: geo.size.width * 0.8, height: geo.size.height * 0.15)
            .clipShape(RoundedRectangle(cornerRadius: 20, style: .continuous))
            .shadow(color: .black.opacity(0.6), radius: 60, x: 0, y: 0)

            .overlay(
              VStack(spacing: 15) {
                Text("UPCOMING")
                  .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 20))
                  .foregroundColor(.white)
                  .multilineTextAlignment(.center)

                Rectangle()
                  .fill(.white)
                  .frame(width: geo.size.width * 0.65, height: 1.5)

                Text("3 MILE KENYAN")
                  .font(.custom("MADEOkineSansPERSONALUSE-Bold", size: 16))
                  .foregroundColor(.white)
                  .multilineTextAlignment(.center)
              })
        }
        .padding(.bottom, 50)
        .overlay(
          CalendarButton(action: onCalendarTapped)
            .padding(.top, geo.safeAreaInsets.top + 10),

          alignment: .topLeading
        )
        .overlay(
          ProfileButton(action: onProfileTapped)
            .padding(.top, geo.safeAreaInsets.top + 10),

          alignment: .topTrailing
        )
      }
      .ignoresSafeArea()

    }
  }
}
