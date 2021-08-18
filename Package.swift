// swift-tools-version:5.4

import PackageDescription


let package = Package(
        name: "App",
        platforms: [
            .macOS(.v10_15),
        ],
        dependencies: [
            .package(url: "https://github.com/vapor/vapor.git", from: "4.0.0"),
            .package(url: "https://github.com/vapor/fluent.git", from: "4.0.0"),
            .package(url: "https://github.com/vapor/fluent-mongo-driver.git", from: "1.0.0"),
            .package(url: "https://github.com/vapor/redis.git", from: "4.0.0"),
            .package(url: "ssh://git@github.com/paulyhedral/sweetrpg-common.git", .branch("develop")),
            .package(url: "ssh://git@github.com/paulyhedral/sweetrpg-api-common.git", .branch("develop")),
            .package(url: "ssh://git@github.com/paulyhedral/sweetrpg-library-model.git", .branch("develop")),
        ],
        targets: [
            .target(name: "App",
                    dependencies: [
                        .product(name: "Common", package: "sweetrpg-common"),
                        .product(name: "APICommon", package: "sweetrpg-api-common"),
                        .product(name: "LibraryModel", package: "sweetrpg-library-model"),
                        .product(name: "Fluent", package: "fluent"),
                        .product(name: "FluentMongoDriver", package: "fluent-mongo-driver"),
                        .product(name: "Vapor", package: "vapor"),
                        .product(name: "Redis", package: "redis"),
                    ],
                    swiftSettings: [
                        // Enable better optimizations when building in Release configuration. Despite the use of
                        // the `.unsafeFlags` construct required by SwiftPM, this flag is recommended for Release
                        // builds. See <https://github.com/swift-server/guides/blob/main/docs/building.md#building-for-production> for details.
                        .unsafeFlags([ "-cross-module-optimization" ], .when(configuration: .release)),
                    ]
            ),
            .executableTarget(name: "Run", dependencies: [ .target(name: "App") ]),
            .testTarget(name: "AppTests", dependencies: [
                .target(name: "App"),
                .product(name: "XCTVapor", package: "vapor"),
            ]),
        ]
)

// Prometheus
// Logging
// Stripe
// Auth0
// APM (NewRelic?)
// Sentry?
