import { all } from "axios";
import {
  take,
  takeLeading,
  takeEvery,
  takeLatest,
  put,
  call,
  fork,
  select,
} from "redux-saga/effects";
import {
  getCurrentUser,
  getDialogById,
  getDialogMessages,
  getUserDialogs,
  sendMessage,
} from "../../api";

import {
  addNewMessage,
  // fetchMessages,
  sendNewMessage,
  setUserInfo,
  setCurrentDialog,
  setDialogs,
  setMessages,
  getCurrentDialog,
  fetchDialog,
  onLoad,
} from "../actions";
import { GET_CURRENT_DIALOG, ON_LOAD } from "../constants";

export function* handleUserInfo() {
  try {
    /**
     * получаем инфу о текущем авторизованном юзере и сохраняем ее в стор
     */
    const userInfo = yield call(getCurrentUser);
    yield put(setUserInfo(userInfo));

    yield call(handleUserDialogs, userInfo.id);
    console.log("after handleUserInfo");
    // yield call(fetchDialogInfoById);
  } catch (error) {
    throw new Error(`Error while getting current user info: ${error}`);
  }
}

export function* handleUserDialogs(userId: number) {
  try {
    /**
     * получаем диалоги текущего юзера и сохраняем их в стор
     */
    const userDialogs = yield call(getUserDialogs);
    yield put(setDialogs(userDialogs));
  } catch (error) {
    throw new Error(`Error while getting current user dialogs: ${error}`);
  }
}

export function* fetchDialogMessages(action) {
  try {
    const messages = yield getDialogMessages(action.payload);
    yield put(setMessages(messages));
  } catch {
    throw new Error("Error while getting current user");
  }
}

export function* onSendNewMessage(action) {
  try {
    const { success } = yield sendMessage(action.payload);
  } catch {
    throw new Error("Error while getting current user");
  }
}

export function* handleCurrentDialog({ payload }) {
  try {
    const currentUser = yield select((state) => state.user);
    if (!currentUser.id) yield call(handleUserInfo);
    // yield take(ON_LOAD);
    yield put(fetchDialog());
    const user = yield select(({ user }) => user);
    // const { first_user_fio, second_user_fio, dialog_id } = yield call(
    //   getDialogById,
    //   payload
    // );

    // yield all([])
    const { first_user_fio, second_user_fio, dialog_id } = yield call(
      getDialogById,
      payload
    );

    let companion;
    if (first_user_fio === `${user.name} ${user.surname}`) {
      companion = second_user_fio;
    } else {
      companion = first_user_fio;
    }

    yield put(setCurrentDialog({ companion, dialogId: payload }));
    const messages = yield call(getDialogMessages, payload);

    // yield fork(fetchMessages(dialog_id));
    yield put(setMessages(messages));
  } catch {
    throw new Error("Error while getting current dialog");
  }
}

export default function* rootSaga() {
  yield takeLatest(ON_LOAD, handleUserInfo);
  // yield takeLatest(fetchDialog, fetchDialogMessages);
  yield takeLatest(sendNewMessage, onSendNewMessage);
  yield takeLatest(getCurrentDialog, handleCurrentDialog);
}
