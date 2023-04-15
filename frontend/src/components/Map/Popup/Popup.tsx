import React, { useState } from "react";
import Avatar from "src/components/Chat/Avatar/Avatar";
import tripIcon from "../../../../static/photos/Tripoholics-icon-white.png";
import countriesIcon from "../../../../static/photos/countries.png";
import citiesIcon from "../../../../static/photos/cities.png";
import { Oval } from "react-loader-spinner";
import "./Popup.scss";
import axios from "axios";
import { useDispatch, useSelector } from "react-redux";
import { createNewDialog } from "src/redux/actions";
import { RootState } from "src/redux/store";

function Popup() {
  const dispatch = useDispatch();
  const isLoadingNewDialog = useSelector(
    (state: RootState) => state.chat.isCreatingNewDialog
  );

  const handleWriteClick = () => {
    console.log("handleWriteClick");
    const data = { interlocutor_id: 9, author_id: 8 };
    // @ts-ignore
    dispatch(createNewDialog(data));
  };

  return (
    <div className="map__popup-wrapper">
      <div className="map__popup-left-block">
        <div className="map__popup-avatar">
          <Avatar width={90} height={90} isOnline={false} letter="Q" isSquare />
        </div>
        <div className="map__popup-descr">
          <div className="map__popup-descr-item descr-countries">
            <img src={countriesIcon} alt="" />
            <p className="map__popup-descr-countries-count">10</p>
          </div>
          <div className="map__popup-descr-item descr-cities">
            <img src={citiesIcon} alt="" />
            <p className="map__popup-descr-cities-count">34</p>
          </div>
        </div>
      </div>
      <div className="map__popup-right-block">
        <div className="map__popup-user">
          <div>
            <p className="map__popup-user-fio">Тест Тестов</p>
            <p className="map__popup-user-nickname">@testtestov</p>
          </div>
          <div className="map__popup-icon">
            <img src={tripIcon} alt="" />
          </div>
        </div>
        <div className="map__popup-info"></div>
        <div className="map__popup-btns">
          <button className="map__popup-btn profile-btn">Профиль</button>
          <button
            className="map__popup-btn message-btn"
            onClick={handleWriteClick}
          >
            {isLoadingNewDialog ? (
              <Oval
                height={20}
                width={20}
                color="#4fa94d"
                wrapperStyle={{}}
                wrapperClass=""
                visible={true}
                ariaLabel="oval-loading"
                secondaryColor="#4fa94d"
                strokeWidth={2}
                strokeWidthSecondary={2}
              />
            ) : (
              "Написать"
            )}
          </button>
        </div>
      </div>
    </div>
  );
}

export default Popup;
