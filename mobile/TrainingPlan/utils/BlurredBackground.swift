import SwiftUI
import UIKit

/* An absolutely disgusting file to write, that creates a blur but with a clear background rather than the frosted glass effect*/
struct BlurEffect: UIViewRepresentable {
  var style: UIBlurEffect.Style = .regular

  func makeUIView(context: Context) -> UIVisualEffectView {
    let blur = UIBlurEffect(style: style)
    let view = UIVisualEffectView(effect: blur)
    view.autoresizingMask = [.flexibleWidth, .flexibleHeight]
    /* Hard override the background tint*/
    view.backgroundColor = .clear
    return view
  }

  func updateUIView(_ uiView: UIVisualEffectView, context: Context) {
    uiView.effect = UIBlurEffect(style: style)

    // HACK: find the private subview (`_UIVisualEffectSubview`)
    // and remove its background so there's no white/grey overlay
    // Thanks Chat :))
    DispatchQueue.main.async {
      if let subview = uiView.subviews.first(where: {
        String(describing: type(of: $0)) == "_UIVisualEffectSubview"
      }) {
        subview.backgroundColor = .clear
      }

    }
  }
}
