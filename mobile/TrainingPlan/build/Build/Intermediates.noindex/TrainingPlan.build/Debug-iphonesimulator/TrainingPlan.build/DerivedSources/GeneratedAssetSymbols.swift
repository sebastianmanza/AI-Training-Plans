import Foundation
#if canImport(AppKit)
import AppKit
#endif
#if canImport(UIKit)
import UIKit
#endif
#if canImport(SwiftUI)
import SwiftUI
#endif
#if canImport(DeveloperToolsSupport)
import DeveloperToolsSupport
#endif

#if SWIFT_PACKAGE
private let resourceBundle = Foundation.Bundle.module
#else
private class ResourceBundleClass {}
private let resourceBundle = Foundation.Bundle(for: ResourceBundleClass.self)
#endif

// MARK: - Color Symbols -

@available(iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, *)
extension DeveloperToolsSupport.ColorResource {

    /// The "accentColor" asset catalog color resource.
    static let accent = DeveloperToolsSupport.ColorResource(name: "accentColor", bundle: resourceBundle)

    /// The "backgroundColor" asset catalog color resource.
    static let background = DeveloperToolsSupport.ColorResource(name: "backgroundColor", bundle: resourceBundle)

    /// The "secondaryColor" asset catalog color resource.
    static let secondary = DeveloperToolsSupport.ColorResource(name: "secondaryColor", bundle: resourceBundle)

    /// The "titleTextColor" asset catalog color resource.
    static let titleText = DeveloperToolsSupport.ColorResource(name: "titleTextColor", bundle: resourceBundle)

}

// MARK: - Image Symbols -

@available(iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, *)
extension DeveloperToolsSupport.ImageResource {

    /// The "Logo" asset catalog image resource.
    static let logo = DeveloperToolsSupport.ImageResource(name: "Logo", bundle: resourceBundle)

    /// The "background" asset catalog image resource.
    static let background = DeveloperToolsSupport.ImageResource(name: "background", bundle: resourceBundle)

    /// The "signupBackground" asset catalog image resource.
    static let signupBackground = DeveloperToolsSupport.ImageResource(name: "signupBackground", bundle: resourceBundle)

    /// The "surveyBackground" asset catalog image resource.
    static let surveyBackground = DeveloperToolsSupport.ImageResource(name: "surveyBackground", bundle: resourceBundle)

    /// The "surveyQuestionBackground" asset catalog image resource.
    static let surveyQuestionBackground = DeveloperToolsSupport.ImageResource(name: "surveyQuestionBackground", bundle: resourceBundle)

}

// MARK: - Color Symbol Extensions -

#if canImport(AppKit)
@available(macOS 14.0, *)
@available(macCatalyst, unavailable)
extension AppKit.NSColor {

    /// The "accentColor" asset catalog color.
    static var accent: AppKit.NSColor {
#if !targetEnvironment(macCatalyst)
        .init(resource: .accent)
#else
        .init()
#endif
    }

    /// The "backgroundColor" asset catalog color.
    static var background: AppKit.NSColor {
#if !targetEnvironment(macCatalyst)
        .init(resource: .background)
#else
        .init()
#endif
    }

    /// The "secondaryColor" asset catalog color.
    static var secondary: AppKit.NSColor {
#if !targetEnvironment(macCatalyst)
        .init(resource: .secondary)
#else
        .init()
#endif
    }

    /// The "titleTextColor" asset catalog color.
    static var titleText: AppKit.NSColor {
#if !targetEnvironment(macCatalyst)
        .init(resource: .titleText)
#else
        .init()
#endif
    }

}
#endif

#if canImport(UIKit)
@available(iOS 17.0, tvOS 17.0, *)
@available(watchOS, unavailable)
extension UIKit.UIColor {

    /// The "accentColor" asset catalog color.
    static var accent: UIKit.UIColor {
#if !os(watchOS)
        .init(resource: .accent)
#else
        .init()
#endif
    }

    /// The "backgroundColor" asset catalog color.
    static var background: UIKit.UIColor {
#if !os(watchOS)
        .init(resource: .background)
#else
        .init()
#endif
    }

    /// The "secondaryColor" asset catalog color.
    static var secondary: UIKit.UIColor {
#if !os(watchOS)
        .init(resource: .secondary)
#else
        .init()
#endif
    }

    /// The "titleTextColor" asset catalog color.
    static var titleText: UIKit.UIColor {
#if !os(watchOS)
        .init(resource: .titleText)
#else
        .init()
#endif
    }

}
#endif

#if canImport(SwiftUI)
@available(iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, *)
extension SwiftUI.Color {

    /// The "accentColor" asset catalog color.
    static var accent: SwiftUI.Color { .init(.accent) }

    /// The "backgroundColor" asset catalog color.
    static var background: SwiftUI.Color { .init(.background) }

    #warning("The \"secondaryColor\" color asset name resolves to a conflicting Color symbol \"secondary\". Try renaming the asset.")

    /// The "titleTextColor" asset catalog color.
    static var titleText: SwiftUI.Color { .init(.titleText) }

}

@available(iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, *)
extension SwiftUI.ShapeStyle where Self == SwiftUI.Color {

    /// The "accentColor" asset catalog color.
    static var accent: SwiftUI.Color { .init(.accent) }

    /// The "backgroundColor" asset catalog color.
    static var background: SwiftUI.Color { .init(.background) }

    /// The "titleTextColor" asset catalog color.
    static var titleText: SwiftUI.Color { .init(.titleText) }

}
#endif

// MARK: - Image Symbol Extensions -

#if canImport(AppKit)
@available(macOS 14.0, *)
@available(macCatalyst, unavailable)
extension AppKit.NSImage {

    /// The "Logo" asset catalog image.
    static var logo: AppKit.NSImage {
#if !targetEnvironment(macCatalyst)
        .init(resource: .logo)
#else
        .init()
#endif
    }

    /// The "background" asset catalog image.
    static var background: AppKit.NSImage {
#if !targetEnvironment(macCatalyst)
        .init(resource: .background)
#else
        .init()
#endif
    }

    /// The "signupBackground" asset catalog image.
    static var signupBackground: AppKit.NSImage {
#if !targetEnvironment(macCatalyst)
        .init(resource: .signupBackground)
#else
        .init()
#endif
    }

    /// The "surveyBackground" asset catalog image.
    static var surveyBackground: AppKit.NSImage {
#if !targetEnvironment(macCatalyst)
        .init(resource: .surveyBackground)
#else
        .init()
#endif
    }

    /// The "surveyQuestionBackground" asset catalog image.
    static var surveyQuestionBackground: AppKit.NSImage {
#if !targetEnvironment(macCatalyst)
        .init(resource: .surveyQuestionBackground)
#else
        .init()
#endif
    }

}
#endif

#if canImport(UIKit)
@available(iOS 17.0, tvOS 17.0, *)
@available(watchOS, unavailable)
extension UIKit.UIImage {

    /// The "Logo" asset catalog image.
    static var logo: UIKit.UIImage {
#if !os(watchOS)
        .init(resource: .logo)
#else
        .init()
#endif
    }

    /// The "background" asset catalog image.
    static var background: UIKit.UIImage {
#if !os(watchOS)
        .init(resource: .background)
#else
        .init()
#endif
    }

    /// The "signupBackground" asset catalog image.
    static var signupBackground: UIKit.UIImage {
#if !os(watchOS)
        .init(resource: .signupBackground)
#else
        .init()
#endif
    }

    /// The "surveyBackground" asset catalog image.
    static var surveyBackground: UIKit.UIImage {
#if !os(watchOS)
        .init(resource: .surveyBackground)
#else
        .init()
#endif
    }

    /// The "surveyQuestionBackground" asset catalog image.
    static var surveyQuestionBackground: UIKit.UIImage {
#if !os(watchOS)
        .init(resource: .surveyQuestionBackground)
#else
        .init()
#endif
    }

}
#endif

// MARK: - Thinnable Asset Support -

@available(iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, *)
@available(watchOS, unavailable)
extension DeveloperToolsSupport.ColorResource {

    private init?(thinnableName: Swift.String, bundle: Foundation.Bundle) {
#if canImport(AppKit) && os(macOS)
        if AppKit.NSColor(named: NSColor.Name(thinnableName), bundle: bundle) != nil {
            self.init(name: thinnableName, bundle: bundle)
        } else {
            return nil
        }
#elseif canImport(UIKit) && !os(watchOS)
        if UIKit.UIColor(named: thinnableName, in: bundle, compatibleWith: nil) != nil {
            self.init(name: thinnableName, bundle: bundle)
        } else {
            return nil
        }
#else
        return nil
#endif
    }

}

#if canImport(AppKit)
@available(macOS 14.0, *)
@available(macCatalyst, unavailable)
extension AppKit.NSColor {

    private convenience init?(thinnableResource: DeveloperToolsSupport.ColorResource?) {
#if !targetEnvironment(macCatalyst)
        if let resource = thinnableResource {
            self.init(resource: resource)
        } else {
            return nil
        }
#else
        return nil
#endif
    }

}
#endif

#if canImport(UIKit)
@available(iOS 17.0, tvOS 17.0, *)
@available(watchOS, unavailable)
extension UIKit.UIColor {

    private convenience init?(thinnableResource: DeveloperToolsSupport.ColorResource?) {
#if !os(watchOS)
        if let resource = thinnableResource {
            self.init(resource: resource)
        } else {
            return nil
        }
#else
        return nil
#endif
    }

}
#endif

#if canImport(SwiftUI)
@available(iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, *)
extension SwiftUI.Color {

    private init?(thinnableResource: DeveloperToolsSupport.ColorResource?) {
        if let resource = thinnableResource {
            self.init(resource)
        } else {
            return nil
        }
    }

}

@available(iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, *)
extension SwiftUI.ShapeStyle where Self == SwiftUI.Color {

    private init?(thinnableResource: DeveloperToolsSupport.ColorResource?) {
        if let resource = thinnableResource {
            self.init(resource)
        } else {
            return nil
        }
    }

}
#endif

@available(iOS 17.0, macOS 14.0, tvOS 17.0, watchOS 10.0, *)
@available(watchOS, unavailable)
extension DeveloperToolsSupport.ImageResource {

    private init?(thinnableName: Swift.String, bundle: Foundation.Bundle) {
#if canImport(AppKit) && os(macOS)
        if bundle.image(forResource: NSImage.Name(thinnableName)) != nil {
            self.init(name: thinnableName, bundle: bundle)
        } else {
            return nil
        }
#elseif canImport(UIKit) && !os(watchOS)
        if UIKit.UIImage(named: thinnableName, in: bundle, compatibleWith: nil) != nil {
            self.init(name: thinnableName, bundle: bundle)
        } else {
            return nil
        }
#else
        return nil
#endif
    }

}

#if canImport(AppKit)
@available(macOS 14.0, *)
@available(macCatalyst, unavailable)
extension AppKit.NSImage {

    private convenience init?(thinnableResource: DeveloperToolsSupport.ImageResource?) {
#if !targetEnvironment(macCatalyst)
        if let resource = thinnableResource {
            self.init(resource: resource)
        } else {
            return nil
        }
#else
        return nil
#endif
    }

}
#endif

#if canImport(UIKit)
@available(iOS 17.0, tvOS 17.0, *)
@available(watchOS, unavailable)
extension UIKit.UIImage {

    private convenience init?(thinnableResource: DeveloperToolsSupport.ImageResource?) {
#if !os(watchOS)
        if let resource = thinnableResource {
            self.init(resource: resource)
        } else {
            return nil
        }
#else
        return nil
#endif
    }

}
#endif

