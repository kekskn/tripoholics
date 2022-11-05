export default function maxMessageLengthCalc(message) {
  return `${message.slice(0, 40)}...`;
}
