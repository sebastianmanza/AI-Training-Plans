import SwiftUI

struct PageIndicatorStyle: View {
  @Binding var selectedIndex: Int
  let selectedColor: Color
  let unselectedColor: Color
  let dotSize: CGFloat
  let numDots: Int
  let dotSpacing: CGFloat

  var body: some View {
    HStack(spacing: dotSpacing) {
      ForEach(0..<numDots, id: \.self) { idx in
        Circle()
          .fill(idx == selectedIndex ? selectedColor : unselectedColor)
          .frame(width: dotSize, height: dotSize)
          .animation(.easeInOut(duration: 0.2), value: selectedIndex)
      }
    }
    .padding(8)
    // .background(Capsule().fill(unselectedColor.opacity(0.2)))
  }
}
