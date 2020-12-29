#!/bin/bash
set -e

# Apply tags
GIT_SHA_TAG=${GITHUB_SHA:0:12}
docker tag $IMAGE_NAME "$DOCKER_REPO:$GIT_SHA_TAG"

# Update index
INDEX_ROW="|\`${BUILD_TIMESTAMP}\`|\`jupyter/${IMAGE_SHORT_NAME}:${GIT_SHA_TAG}\`|[Git diff](https://github.com/jupyter/docker-stacks/commit/${GITHUB_SHA})<br />[Dockerfile](https://github.com/jupyter/docker-stacks/blob/${GITHUB_SHA}/${IMAGE_SHORT_NAME}/Dockerfile)<br />[Build manifest](./${IMAGE_SHORT_NAME}-${GIT_SHA_TAG})|"
sed "/|-|/a ${INDEX_ROW}" -i "${WIKI_PATH}/Home.md"

# Build manifest
MANIFEST_FILE="${WIKI_PATH}/manifests/${IMAGE_SHORT_NAME}-${GIT_SHA_TAG}.md"
mkdir -p $(dirname "$MANIFEST_FILE")

cat << EOF > "$MANIFEST_FILE"
* Build datetime: ${BUILD_TIMESTAMP}
* Docker image: ${DOCKER_REPO}:${GIT_SHA_TAG}
* Docker image size: $(docker images ${IMAGE_NAME} --format "{{.Size}}")
* Git commit SHA: [${GITHUB_SHA}](https://github.com/jupyter/docker-stacks/commit/${GITHUB_SHA})
* Git commit message:
\`\`\`
${COMMIT_MSG}
\`\`\`
## Python Packages
\`\`\`
$(docker run --rm ${IMAGE_NAME} python --version)
\`\`\`
\`\`\`
$(docker run --rm ${IMAGE_NAME} conda info)
\`\`\`
\`\`\`
$(docker run --rm ${IMAGE_NAME} conda list)
\`\`\`
## Apt Packages
\`\`\`
$(docker run --rm ${IMAGE_NAME} apt list --installed)
\`\`\`
EOF