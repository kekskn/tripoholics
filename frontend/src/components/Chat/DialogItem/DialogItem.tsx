import React, { useState } from "react";
import { formatDistance, subDays } from "date-fns";
import ru from "date-fns/esm/locale/ru/index.js";

import Avatar from "../Avatar/Avatar";
import maxMessageLengthCalc from "../../../utils/maxMessageLengthCalc";

import "./DialogItem.scss";
import { NavLink } from "react-router-dom";

export default function DialogItem({
  date,
  roomName,
  companion,
  dialogId,
  isEmptyDialog,
}) {
  const [isActiveDialog, setIsActiveDialog] = useState(false);
  let activeStyle = {
    textDecoration: "none",
  };
  let notActiveStyle = {
    textDecoration: "none",
    color: "inherit",
  };

  return (
    <NavLink
      to={`/my_messages/${isEmptyDialog ? `new_dialog/${dialogId}` : dialogId}`}
      className="dialog-item-link"
      style={({ isActive }) => {
        if (isActive) {
          setIsActiveDialog(true);
          return activeStyle;
        } else {
          setIsActiveDialog(false);
          return notActiveStyle;
        }
      }}
    >
      <div className="dialog-item">
        <div className="dialog-item__avatar">
          <Avatar height={48} width={48} isOnline letter={companion[0]} />
        </div>
        <div className="dialog-item__info-wrapper">
          <div className="dialog-item__info">
            <div className="dialog-item__fullname">{companion}</div>
            <div className="dialog-item__date">
              {formatDistance(date, new Date(), {
                addSuffix: true,
                locale: ru,
              })}
            </div>
          </div>
          <div className="dialog-item__messages">
            <div className="dialog-item__last-message">
              {maxMessageLengthCalc("Приветик, как дела? Я тут вспомнил")}
            </div>
            {!isActiveDialog && (
              <div className="dialog-item__unread-messages">3</div>
            )}
          </div>
        </div>
      </div>
    </NavLink>
  );
}
