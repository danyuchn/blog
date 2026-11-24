/** Signature groups for the zh "my work" page. Copy is fixed; do not reword. */

export type SignatureId =
  | "1"
  | "2"
  | "3"
  | "4"
  | "5"
  | "6"
  | "7"
  | "8"
  | "9"
  | "10"
  | "11"
  | "12"
  | "13"
  | "other";

export type SignatureEntry = {
  id: SignatureId;
  name: string;
  /** Omitted for "other", which only lists posts. */
  oneLiner?: string;
};

export const SIGNATURES: SignatureEntry[] = [
  {
    id: "1",
    name: "戒掉 AI 官腔的工具",
    oneLiner: "用國際白話文標準綁住 AI，逼它講人話、不准寫空洞套話。",
  },
  {
    id: "2",
    name: "給分心大腦的 AI 協作法",
    oneLiner: "注意力容易散掉？換一套不靠意志力硬撐的 AI 工作方式。",
  },
  {
    id: "3",
    name: "規則消融實驗",
    oneLiner: "把給 AI 的規則先砍光，看哪些拿掉才會出事，徹底清掉沒用的設定。",
  },
  {
    id: "4",
    name: "選擇題終結審閱頁",
    oneLiner: "拒看 AI 吐出的長篇問答，直接轉成點按鈕就能一路批完的網頁。",
  },
  {
    id: "5",
    name: "個人系統卡",
    oneLiner: "一張卡讓 AI 認清你是誰，省下每天重複交代背景的冤枉時間。",
  },
  {
    id: "6",
    name: "決定判例庫",
    oneLiner: "你拍板過的事不該重問第二次。把過去的決定存成判例，讓 AI 照抄。",
  },
  {
    id: "7",
    name: "可逆與不可逆的放手線",
    oneLiner: "能退回的直接放手，不能退回的才親自審，不再每件事都自己盯。",
  },
  {
    id: "8",
    name: "防話癆收斂模式",
    oneLiner: "專治 AI 東拉西扯與過度發散，讓它每次只交出你要的結果。",
  },
  {
    id: "9",
    name: "個人 AI 決策工作台",
    oneLiner: "用嘴巴派工、讓看板管待辦與知識庫，把日常瑣事收進同一套系統。",
  },
  {
    id: "10",
    name: "送進 AI 前的個資遮罩",
    oneLiner: "資料餵給 AI 前先去識別化，針對台灣常見個資格式直接擋在門外。",
  },
  {
    id: "11",
    name: "模型體檢與分工術",
    oneLiner: "不看行銷話術，直接讀模型系統卡挑主力，讓不同 AI 分工合作。",
  },
  {
    id: "12",
    name: "零程式背景的 AI 教學規格",
    oneLiner: "從上課逐字稿提煉教法，回答「老師與外行人該怎麼面對 AI」。",
  },
  {
    id: "13",
    name: "企業導入與接案真實復盤",
    oneLiner: "不講成功學，攤開企業培訓與接案現場真正遇到的問題與解法。",
  },
  {
    id: "other",
    name: "其他自製工具",
  },
];
