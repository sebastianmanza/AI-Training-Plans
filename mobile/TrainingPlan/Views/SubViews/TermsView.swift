import SwiftUI

/* A view that displays the terms and conditions for the Endorphin app. */
struct TermsView: View {
  var body: some View {
    ScrollView {
      VStack(alignment: .leading, spacing: 16) {
        Text("TERMS AND CONDITIONS")
          .font(.title)
          .bold()
          .padding(.bottom, 10)

        Group {
          Text(
            "Welcome to Endorphin. By using this app, you agree to the following terms and conditions. If you do not agree, please do not use the app."
          )

          Text("1. No Medical Advice")
            .font(.headline)
          Text(
            "The Endorphin app is for informational and educational purposes only. It does not provide medical advice, diagnosis, or treatment. Always consult your physician or a qualified health provider before beginning any exercise program or making changes to your health regimen."
          )

          Text("2. Assumption of Risk")
            .font(.headline)
          Text(
            "By using this app, you acknowledge and agree that physical activity involves inherent risks, including injury, illness, or death. You voluntarily assume full responsibility for any risks, known or unknown, associated with your use of this app and its content."
          )

          Text("3. No Guarantees")
            .font(.headline)
          Text(
            "We do not guarantee that our recommendations will lead to any specific fitness or health outcome. All results vary based on individual conditions and effort."
          )

          Text("4. Limitation of Liability")
            .font(.headline)
          Text(
            "To the fullest extent permitted by law, Endorphin, its creators, affiliates, and partners shall not be liable for any direct, indirect, incidental, consequential, special, or punitive damages, including but not limited to injury, loss of use, data, or profits, arising out of or related to your use of the app."
          )

          Text("5. No Warranty")
            .font(.headline)
          Text(
            "This app and its content are provided “as is” and without warranties of any kind, whether express or implied."
          )

          Text("6. User Responsibility")
            .font(.headline)
          Text(
            "You are solely responsible for your health, actions, and any consequences that arise from following advice or plans provided in this app."
          )

          Text("7. Changes to These Terms")
            .font(.headline)
          Text(
            "We reserve the right to update or modify these Terms at any time without prior notice. Continued use of the app after changes constitutes acceptance of the new terms."
          )

          Text("8. Contact")
            .font(.headline)
          Text(
            "If you have any questions or concerns about these Terms, please contact us at [Insert Email or Contact Info]."
          )
        }

        Text(
          "By using this app, you acknowledge that you have read, understood, and agreed to these terms and conditions."
        )
      }
      .padding()
    }
    .navigationTitle("Terms & Conditions")
  }
}