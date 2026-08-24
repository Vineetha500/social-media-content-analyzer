import {
  Lightbulb,
} from "lucide-react";


export default function SuggestionCard({
  suggestion,
}) {

  return (
    <div className="suggestion-card">

      <div className="suggestion-icon">
        <Lightbulb size={20} />
      </div>

      <p>
        {suggestion}
      </p>

    </div>
  );
}