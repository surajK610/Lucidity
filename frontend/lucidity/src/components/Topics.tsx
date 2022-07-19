import React, { useState, useEffect } from 'react';
import './Topics.css';
import ReactApexChart from 'react-apexcharts';
import { ApexOptions } from 'apexcharts';
import '../types.d.ts';

type TopicProps = {
  topicList: Topic[];
};

function Topics(props: TopicProps) {
  const [chartState, setChartState] = useState<ApexOptions | null>(null);

  useEffect(() => {
    console.log('creating piechart');
    calcOther();
  }, []);

  const calcOther = () => {
    let otherVal: number = 100;
    let freqs: number[] = [];
    let topics: string[] = [];
    for (var tDict of props.topicList) {
      otherVal = otherVal - tDict.frequency;
      freqs.push(tDict.frequency);
      topics.push(tDict.topic);
    }
    freqs.push(otherVal);
    topics.push('Other');
    console.log(freqs);
    console.log(topics);

    const state = {
      series: freqs,
      labels: topics,
      options: {
        chart: {
          width: 380,
          length: 380,
          type: 'pie',
        },
        // series: freqs,
        labels: topics,
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
    <div>
      <div className="topics-page-container">
        <div className="topics-text-container">
          <div className="topics__title">Topic Time!</div>
          <div className="topics__subtitle">
            Here are the topics you discussed the most in your text messages
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
    </div>
  );
}

export default Topics;
