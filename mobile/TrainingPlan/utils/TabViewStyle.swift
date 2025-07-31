import SwiftUI

struct TabViewStyle: View {
  @Binding var selectedIndex: Int
  let accentColor: Color
  let backgroundColor: Color
  let dotSize: CGFloat
  let numDots: Int

  var body: some View {
    HStack(spacing: dotSpacing) {
      ForEach(numDots, id: \.self) { idx in
        Circle()
          .fill(
            idx == selectedIndex
              ? accentColor
              : backgroundColor
          )
          .frame(width: dotSize, height: dotSize)
      }
    }
  }
}
