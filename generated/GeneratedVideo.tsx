import React from "react";
import {
    AbsoluteFill,
    Sequence,
    Img,
    staticFile
} from "remotion";

interface StoryboardScene {
    image: string;
    start_time: number;
    duration: number;
    caption: string;
    transition: string;
    reason: string;
}

interface GeneratedVideoProps {
    scenes: StoryboardScene[];
}

export const GeneratedVideo: React.FC<GeneratedVideoProps> = ({ scenes }) => {
    return (
        <AbsoluteFill style={{ backgroundColor: "black" }}>
            {scenes.map((scene, index) => {
                const fromFrames = scene.start_time * 30;
                const durationFrames = scene.duration * 30;

                return (
                    <Sequence
                        key={index}
                        from={fromFrames}
                        durationInFrames={durationFrames}
                    >
                        <Img
                            src={staticFile(scene.image)}
                            style={{
                                width: "100%",
                                height: "100%",
                                objectFit: "cover"
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
                                textShadow: "2px 2px 4px rgba(0,0,0,0.7)"
                            }}
                        >
                            {scene.caption}
                        </div>
                    </Sequence>
                );
            })}
        </AbsoluteFill>
    );
};