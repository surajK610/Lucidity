type ContactResponseTime = {
  name: string;
  responseTime: string;
};

type Sentiment = {
  positive: string;
  negative: string;
  neutral: string;
};

type ContactEmojis = {
  name: string;
  rate: number;
  emojis: string;
};

type Emotion = {
  emotion: string;
  frequency: number;
};

type Topic = {
  topic: string;
  frequency: number;
};

type CelebMatch = {
  name: string;
  matchPercent: string;
  imgPath: string;
};

type WordFreq = {
  text: string;
  value: number;
};

type User = {
  _id: string;
  name: string;
  email: string;
  avgResponseTime: string;
  contactResTimes: ContactResponseTime[];
  avgTextLength: number;
  msgFreqDay: number;
  convoInitFreq: string;
  msgSentiment: Sentiment;
  totalMessages: number;
  messagesPerDay: string;
  favEmojis: string;
  emojisByContact: ContactEmojis[];
  emotions: Emotion[];
  topics: Topic[];
  personality: string;
  celebMatches: CelebMatch[];
  wordFreqs: WordFreq[];
  dataList: string[];
};

type ApexOptions = {
  chart: {
    width?: string | number;
    height?: string | number;
    type: string;
    foreColor?: string;
  };
  plotOptions?: {
    radialBar?: {
      offsetY?: number;
      startAngle?: number;
      endAngle?: number;
      hollow?: {
        margin: number;
        size: string;
        background: string;
        image: string | undefined;
      };
      track?: {
        show: boolean;
      };
      dataLabels?: {
        showOn?: string;
        name?: {
          show: boolean;
        };
        value?: {
          show: boolean;
        };
      };
    };
    circle?: {
      track?: {
        show: boolean;
      };
      dataLabels: {
        showOn?: string;
        name?: {
          show: boolean;
        };
        value?: {
          show: boolean;
        };
      };
    };
    pie?: {
      size?: undefined;
      donut?: {
        size?: string;
        background?: string;
      };
      customScale?: number;
      offsetX?: number;
      offsetY?: number;
      dataLabels?: {
        offset?: number;
      };
    };
  };
  colors?: string[];
  series: number[];
  labels?: string[];
  legend?: {
    show?: boolean;
    floating?: boolean;
    fontSize?: string;
    position?: string;
    verticalAlign?: string;
    textAnchor?: string;
    labels?: {
      useSeriesColors: boolean;
    };
    markers?: {
      size: number;
    };
    formatter?: Function;
    itemMargin?: {
      vertical: number;
    };
    containerMargin?: {
      left: number;
      top: number;
    };
  };
};
