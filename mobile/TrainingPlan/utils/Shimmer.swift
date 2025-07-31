import SwiftUI

struct ShimmerModifier: ViewModifier {
  let duration: Double
  let highlight: Color
  let background: Color

  @State private var startPoint = UnitPoint(x: -1.8, y: -1.2)
  @State private var endPoint = UnitPoint(x: 0, y: -0.2)

  init(
    duration: Double = 1.5,
    highlight: Color = .white.opacity(0.8),
    background: Color = .gray.opacity(0.25)
  ) {
    self.duration = duration
    self.highlight = highlight
    self.background = background
  }

  func body(content: Content) -> some View {
    content
      .overlay(
        LinearGradient(
          colors: [background, highlight, background],
          startPoint: startPoint,
          endPoint: endPoint
        )
        .mask(content)
        .onAppear {
          withAnimation(
            .easeInOut(duration: duration)
              .repeatForever(autoreverses: false)
          ) {
            startPoint = UnitPoint(x: 1, y: 1.2)
            endPoint = UnitPoint(x: 2.2, y: 2.4)
          }
        }
      )
      .clipped()
  }
}

extension View {
  func shimmer(
    duration: Double = 1.5,
    highlight: Color = .white.opacity(0.8),
    background: Color = .gray.opacity(0.25)
  ) -> some View { 
    modifier(
      ShimmerModifier(
        duration: duration,
        highlight: highlight,
        background: background
      ))
  }
}
