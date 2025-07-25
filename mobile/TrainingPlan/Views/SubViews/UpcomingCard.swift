import SwiftUI

struct UpcomingCard: View {
    let accentColorStart : Color
    let accentColorStop : Color
    let backgroundColor: Color
    let viewWidth: CGFloat
    let viewHeight: CGFloat
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
                .frame(width: viewWidth, height: viewHeight)

            Rectangle()
                .fill(backgroundColor)
                .frame(width: viewWidth - 50, height: viewHeight)

            /* Foreground */
            VStack(alignment: .leading, spacing: 10) {
                if let data = vm.homeData {
                    Text(data.upcoming)
                        .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 20))
                        .foregroundColor(mainTextColor)
                    
                    HStack {
                        Text("Placeholder miles")
                            .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 16))
                            .foregroundColor(accentTextColor)
                        
                        Spacer()
                        
                        Text("Placeholder secondary")
                            .font(.custom("MADEOkineSansPERSONALUSE-Medium", size: 16))
                            .foregroundColor(accentTextColor)
                    }
                    // .padding(.trailing, 30)
                } else {
                    ProgressView()
                        .foregroundColor(.white)
                }
            }
            .padding(.leading, 60)

        }
    }
}
