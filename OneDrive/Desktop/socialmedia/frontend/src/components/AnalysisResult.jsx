import {
  CheckCircle2,
  FileText,
  RotateCcw,
} from "lucide-react";

import ScoreCard from "./ScoreCard";
import SuggestionCard from "./SuggestionCard";


export default function AnalysisResult({
  result,
  onReset,
}) {

  const breakdown =
    result.score_breakdown;


  return (
    <div className="results-container">

      <div className="result-header">

        <div>

          <div className="result-file">

            <FileText size={20} />

            <span>
              {result.filename}
            </span>

          </div>

          <p className="result-type">
            {result.file_type}
          </p>

        </div>

        <button
          className="reset-button"
          onClick={onReset}
        >
          <RotateCcw size={17} />
          Analyze another
        </button>

      </div>


      <div className="top-results">

        <div className="main-score">

          <div className="score-circle">

            <strong>
              {result.engagement_score}
            </strong>

            <span>
              /100
            </span>

          </div>

          <div>
            <h2>
              Engagement Score
            </h2>

            <p>
              Overall content performance
              potential
            </p>
          </div>

        </div>


        <div className="stats">

          <div>
            <span>Words</span>
            <strong>
              {result.word_count}
            </strong>
          </div>

          <div>
            <span>Characters</span>
            <strong>
              {result.character_count}
            </strong>
          </div>

          <div>
            <span>Tone</span>
            <strong>
              {result.tone}
            </strong>
          </div>

        </div>

      </div>


      <section className="section">

        <h2>
          Score Breakdown
        </h2>

        <div className="score-grid">

          <ScoreCard
            title="Hook"
            score={breakdown.hook}
          />

          <ScoreCard
            title="Readability"
            score={breakdown.readability}
          />

          <ScoreCard
            title="Call to Action"
            score={
              breakdown.call_to_action
            }
          />

          <ScoreCard
            title="Hashtags"
            score={breakdown.hashtags}
          />

          <ScoreCard
            title="Engagement"
            score={breakdown.engagement}
          />

        </div>

      </section>


      <section className="section">

        <h2>
          Strengths
        </h2>

        <div className="strength-list">

          {result.strengths.map(
            (strength, index) => (

              <div
                className="strength-item"
                key={index}
              >

                <CheckCircle2 size={20} />

                <span>
                  {strength}
                </span>

              </div>

            )
          )}

        </div>

      </section>


      <section className="section">

        <h2>
          Improvement Suggestions
        </h2>

        <div className="suggestions">

          {result.suggestions.map(
            (suggestion, index) => (

              <SuggestionCard
                key={index}
                suggestion={suggestion}
              />

            )
          )}

        </div>

      </section>


      <section className="section">

        <h2>
          Extracted Text
        </h2>

        <div className="extracted-text">

          <pre>
            {result.extracted_text}
          </pre>

        </div>

      </section>

    </div>
  );
}