import React from "react";

import { Composition } from "remotion";

import { GeneratedVideo } from "../generated/GeneratedVideo";


export const RemotionRoot = () => {

    return (

        <Composition

            id="GeneratedVideo"

            component={GeneratedVideo}

            durationInFrames={120}

            fps={30}

            width={1080}

            height={1920}

        />

    );

};