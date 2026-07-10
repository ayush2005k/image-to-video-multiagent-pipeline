import React from "react";
import {
    AbsoluteFill,
    Sequence,
    Img,
    useCurrentFrame,
    interpolate,
    staticFile
} from "remotion";

export const GeneratedVideo: React.FC = () => {
    return (
        <AbsoluteFill style={{ backgroundColor: "white" }}>
            {/* Scene 1: Beautiful memory */}
            <Sequence from={0} durationInFrames={120}>
                <Scene1Content />
            </Sequence>
        </AbsoluteFill>
    );
};

const Scene1Content: React.FC = () => {
    const frame = useCurrentFrame();

    // Fade transition for the image (fades in over the first 30 frames of the sequence)
    const opacity = interpolate(
        frame,
        [0, 30],
        [0, 1],
        { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
    );

    return (
        <AbsoluteFill>
            <Img
                src={staticFile("IMG_0704.jpg")}
                style={{
                    opacity,
                    width: "100%",
                    height: "100%",
                    objectFit: "cover",
                }}
            />
            <div
                style={{
                    position: "absolute",
                    bottom: 50,
                    width: "100%",
                    textAlign: "center",
                    color: "white",
                    fontSize: 40,
                    fontWeight: "bold",
                    textShadow: "2px 2px 4px rgba(0,0,0,0.5)",
                    opacity: opacity, // Caption also fades in with the image
                }}
            >
                Beautiful memory
            </div>
        </AbsoluteFill>
    );
};