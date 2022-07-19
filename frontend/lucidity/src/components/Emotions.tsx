import React, { useEffect, useState } from 'react';
import ReactApexChart from 'react-apexcharts';
import { ApexOptions } from 'apexcharts';
import './Emotions.css';
import '../types.d.ts';

type EmotionProps = {
  emotionList: Emotion[];
};

function Emotions(props: EmotionProps) {
  const [chartState, setChartState] = useState<ApexOptions | null>(null);

  useEffect(() => {
    console.log('creating piechart');
    calcOther();
  }, []);

  const calcOther = () => {
    let otherVal: number = 100;
    let freqs: number[] = [];
    let emotions: string[] = [];
    for (var eDict of props.emotionList) {
      otherVal = otherVal - eDict.frequency;
      freqs.push(eDict.frequency);
      emotions.push(eDict.emotion);
    }
    freqs.push(otherVal);
    emotions.push('other');
    console.log(freqs);
    console.log(emotions);

    const state = {
      series: freqs,
      labels: emotions,
      options: {
        chart: {
          width: 380,
          length: 380,
          type: 'pie',
        },
        labels: emotions,
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 200,
                length: 200,
              },
              legend: {
                position: 'bottom',
              },
            },
          },
        ],
      },
    };
    setChartState(state);
  };
  return (
    <div className="emotions-page-container">
      <div className="emotions-text-container">
        <div className="emotions__title">Emotion Breakdown</div>
        <div className="emotions__subtitle">
          It's better to see an emotion breakdown than to have an emotional
          breakdown.
          <br />
          Here are the emotions you exhibited the most through your texts
        </div>
      </div>
      {chartState ? (
        <ReactApexChart
          options={chartState}
          series={chartState.series}
          labels={chartState.labels}
          type="pie"
          width={500}
        />
      ) : (
        <>yikes</>
      )}
    </div>
  );
}

export default Emotions;
