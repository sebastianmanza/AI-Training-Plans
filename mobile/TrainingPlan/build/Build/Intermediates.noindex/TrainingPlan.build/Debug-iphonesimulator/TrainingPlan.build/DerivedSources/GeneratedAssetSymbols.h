#import <Foundation/Foundation.h>

#if __has_attribute(swift_private)
#define AC_SWIFT_PRIVATE __attribute__((swift_private))
#else
#define AC_SWIFT_PRIVATE
#endif

/// The resource bundle ID.
static NSString * const ACBundleID AC_SWIFT_PRIVATE = @"MAP.TrainingPlan";

/// The "accentColor" asset catalog color resource.
static NSString * const ACColorNameAccentColor AC_SWIFT_PRIVATE = @"accentColor";

/// The "backgroundColor" asset catalog color resource.
static NSString * const ACColorNameBackgroundColor AC_SWIFT_PRIVATE = @"backgroundColor";

/// The "secondaryColor" asset catalog color resource.
static NSString * const ACColorNameSecondaryColor AC_SWIFT_PRIVATE = @"secondaryColor";

/// The "titleTextColor" asset catalog color resource.
static NSString * const ACColorNameTitleTextColor AC_SWIFT_PRIVATE = @"titleTextColor";

/// The "Logo" asset catalog image resource.
static NSString * const ACImageNameLogo AC_SWIFT_PRIVATE = @"Logo";

/// The "background" asset catalog image resource.
static NSString * const ACImageNameBackground AC_SWIFT_PRIVATE = @"background";

/// The "signupBackground" asset catalog image resource.
static NSString * const ACImageNameSignupBackground AC_SWIFT_PRIVATE = @"signupBackground";

/// The "surveyBackground" asset catalog image resource.
static NSString * const ACImageNameSurveyBackground AC_SWIFT_PRIVATE = @"surveyBackground";

/// The "surveyQuestionBackground" asset catalog image resource.
static NSString * const ACImageNameSurveyQuestionBackground AC_SWIFT_PRIVATE = @"surveyQuestionBackground";

#undef AC_SWIFT_PRIVATE
