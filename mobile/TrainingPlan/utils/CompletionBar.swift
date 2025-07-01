import SwiftUI

struct CompletionBar: View {
    let background: Color
    let fill: Color
    let width: CGFloat
    let height: CGFloat
    let percentComplete: CGFloat

    var body: some View {
        ZStack(alignment: .leading) {
        RoundedRectangle(cornerRadius: (height / 2))
            .fill(background)
            .frame(width: width, height: height)

        RoundedRectangle(cornerRadius: (height / 2))
            .fill(fill)
            .frame(width: (percentComplete * width), height: height)
        }
    }
}
