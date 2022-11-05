import React from "react";
import { formatDistance, subDays } from "date-fns";
import Avatar from "../Avatar/Avatar";

import maxMessageLengthCalc from "../../../utils/maxMessageLengthCalc";

import "./DialogItem.scss";
import ru from "date-fns/esm/locale/ru/index.js";

export default function DialogItem() {
  const date = new Date(2022, 10, 5);
  return (
    <div className="dialog-item">
      <Avatar height={40} width={40} isOnline />
      <div>
        <div className="dialog-item__fullname">Тест Тестов</div>
        <div className="dialog-item__last-message">
          {maxMessageLengthCalc(
            "Lorem ipsum dolor sit amet, consectetur frhicsnjks"
          )}
        </div>
      </div>
      <div className="dialog-item__date">
        {formatDistance(date, new Date(), { addSuffix: true, locale: ru })}
      </div>
    </div>
  );
}
