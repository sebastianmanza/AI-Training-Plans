import SwiftUI

class RPESlider: UISlider {

  /* Overriding the height of the track */
  override func trackRect(forBounds bounds: CGRect) -> CGRect {
    var rect = super.trackRect(forBounds: bounds)
    rect.size.height = 15
    return rect
  }
}

  struct RPESliderView: UIViewRepresentable {
    @Binding var value: Double
    let range: ClosedRange<Double>
    let step: Double

    func makeUIView(context: Context) -> RPESlider {
      let slider = RPESlider(frame: .zero)
      slider.minimumValue = Float(range.lowerBound)
      slider.maximumValue = Float(range.upperBound)
      slider.value = Float(value)
      slider.isContinuous = true
      slider.addTarget(
        context.coordinator,
        action: #selector(Coordinator.valueChanged(_:)),
        for: .valueChanged
      )
      return slider
    }

    func updateUIView(_ uiView: RPESlider, context: Context) {
      let stepped = round(uiView.value / Float(step)) * Float(step)
      if Double(stepped) != value {
        uiView.value = stepped
      }
    }

    func makeCoordinator() -> Coordinator {
      Coordinator(binding: $value, step: step)
    }

    class Coordinator: NSObject {
      var binding: Binding<Double>
      let step: Double

      init(binding: Binding<Double>, step: Double) {
        self.binding = binding
        self.step = step
      }

      @objc func valueChanged(_ sender: UISlider) {
        let newValue = Double(sender.value)
        let stepped = (round(newValue / step) * step)
        binding.wrappedValue = stepped
      }
    }
  }
