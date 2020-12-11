#pragma once

#include "visionbuf.h"
#define VISIONIPC_NUM_BUFS 10

enum VisionStreamType {
  VISION_STREAM_RGB_BACK,
  VISION_STREAM_RGB_FRONT,
  VISION_STREAM_RGB_WIDE,
  VISION_STREAM_YUV,
  VISION_STREAM_YUV_FRONT,
  VISION_STREAM_YUV_WIDE,
  VISION_STREAM_MAX,
};



struct VisionStream {
  VisionStreamType type;
  int width, height, stride;

  int num_bufs;
  int last_idx;

  VisionBuf *bufs;
};


void visionipc_start_server(void);
