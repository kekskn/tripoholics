import { combineReducers } from "redux";
import chatSlice from "./chat";
import mapSlice from "./map";
import userSlice from "./user";

const reducer = combineReducers({
  user: userSlice.reducer,
  chat: chatSlice.reducer,
  map: mapSlice.reducer,
});

export default reducer;
