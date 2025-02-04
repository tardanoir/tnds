"""Use trained model to make predictions."""

from pathlib import Path

import pandas as pd


def load_model():
    """Load the trained model."""
    # project_dir = Path(__file__).resolve().parents[2]
    return None, None


def load_data():
    """Load data to make predictions on."""
    project_dir = Path(__file__).resolve().parents[2]
    data_path = project_dir / "data" / "processed"
    return pd.read_csv(data_path / "features.csv")
    # Example:
    # import pandas as pd
    # data_path = project_dir / 'data' / 'processed'
    # features = pd.read_csv(data_path / 'features.csv')
    return None


def make_predictions(model, scaler, features):
    """Make predictions using the trained model."""
    # Scale the features
    features_scaled = scaler.transform(features)

    # Make predictions
    predictions = model.predict(features_scaled)

    return predictions


def save_predictions(predictions, output_path=None):
    """Save predictions to a file."""
    if output_path is None:
        project_dir = Path(__file__).resolve().parents[2]
        output_path = project_dir / "data" / "predictions" / "predictions.csv"

    # Create predictions directory if it doesn't exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Example:
    # import pandas as pd
    # pd.Series(predictions).to_csv(output_path, index=False)
    pass


def main():
    """Run the prediction pipeline."""
    # Load model and scaler
    model, scaler = load_model()

    # Load data
    features = load_data()

    # Make predictions
    predictions = make_predictions(model, scaler, features)

    # Save predictions
    save_predictions(predictions)


if __name__ == "__main__":
    main()
