
optimal_k = 3    

kmeans = KMeans(
    n_clusters=optimal_k,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_cluster_scaled)

print("First 10 Cluster Assignments:")
print(clusters[:10])

# Display cluster sizes
cluster_counts = pd.Series(clusters).value_counts().sort_index()

print("\nCustomers in Each Cluster:")
print(cluster_counts)

# Save the trained model
joblib.dump(
    kmeans,
    os.path.join(output_dir, "kmeans_model.pkl")
)

# Save the scaler
joblib.dump(
    scaler,
    os.path.join(output_dir, "scaler.pkl")
)

print(f"\nK-Means model with {optimal_k} clusters saved successfully.")
