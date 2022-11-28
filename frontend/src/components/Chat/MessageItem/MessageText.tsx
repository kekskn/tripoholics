import React from "react";
import cn from "classnames";

export default function MessageText({ isRead }) {
  return (
    <div className={cn("message-item__text", { read: isRead })}>
      Привет, как дела? Что делаешь?
    </div>
  );
}
