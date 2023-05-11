import React from "react";
import cn from "classnames";

import letterToNumber from "./helpers/letterToNumber";
import "./Avatar.scss";

type Props = {
  height: number;
  width: number;
  isOnline: boolean;
  letter: string;
  isSquare?: boolean;
  img?: string;
};

export default function Avatar({
  height,
  width,
  isOnline,
  letter,
  isSquare,
  img,
}: Props) {
  return (
    <div
      className={cn("avatar", { online: isOnline })}
      style={{
        height: `${height}px`,
        width: `${width}px`,
        backgroundColor: `hsl(${letterToNumber[letter]}, 60%, 25%)`,
        borderRadius: `${isSquare ? "0" : "50%"}`,
        backgroundImage: `url(${img})`,
        backgroundRepeat: "no-repeat",
        backgroundSize: "cover",
        backgroundPosition: "center",
      }}
    >
      {!img && letter}
    </div>
  );
}
