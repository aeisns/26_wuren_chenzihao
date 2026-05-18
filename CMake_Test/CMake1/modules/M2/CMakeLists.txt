aux_source_directory(src Path_M2)

add_library(M2 STATIC ${Path_M2})

find_package(OpenCV REQUIRED)

target_include_directories(M2 PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include ${CMAKE_CURRENT_SOURCE_DIR}/../../common/kalman/include ${CMAKE_CURRENT_SOURCE_DIR/../A1/include} ${CMAKE_CURRENT_SOURCE_DIR/../A2/include} ${OpenCV_INCLUDE_DIRS})

target_link_libraries(M2 PUBLIC ${OpenCV_LIBS} A1 A2)
