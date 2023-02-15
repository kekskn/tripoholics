import React from "react";
import cn from "classnames";

export default function MessageText({ text, isRead }) {
  return (
    <div className={cn("message-item__text", { read: isRead })}>{text}</div>
  );
}
