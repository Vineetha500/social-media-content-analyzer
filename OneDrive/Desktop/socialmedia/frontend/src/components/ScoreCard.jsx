export default function ScoreCard({
  title,
  score,
}) {

  return (
    <div className="score-card">

      <div className="score-card-header">
        <span>{title}</span>
        <strong>{score}</strong>
      </div>

      <div className="progress-background">

        <div
          className="progress-value"
          style={{
            width: `${score}%`,
          }}
        />

      </div>

    </div>
  );
}