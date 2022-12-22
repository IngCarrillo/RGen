/**
 * @copyright
 * This document is a part of the source code and related artifacts
 * for Modutram Autotr�n transportation system
 *
 * http://www.modutram.com
 *
 * Copyright � 2020 Modutram
 *
 * Any use of this source code - including reproduction, modification, distribution, 
 * republication, transmission, re-transmission, modification, or public showing - without the prior 
 * written permission of Modutram is strictly prohibited. 
 *
 * @file    SIS_MSF031_MINITRAINTAG_def.h
 *
 * @brief   MSF031 -- SIL4 -- Definiciones: Almacenar el identificador de minitren asignado por un SIV-P y mantenerlo hasta que un SIV-P lo sobreescriba.  
 * @note
 *        ______________      ______________      ______________
 *        Juan Aguirre        Luis G�mez          Luis Gonz�lez
 *        Dise�ador           Verificador         PM 
 *
 * @version SIS 
 * - Juan Aguirre -- 09/06/2020 -- db36ee8eebc10
 *   - Primera Versi�n
 *     
 */

#ifndef MINITRAINTAG_def_H_
#define MINITRAINTAG_def_H_

/* system headers */
#include "Std_Types.h"

/* exported macros */

/* exported types */
/**
 * @def MINITRAINTAG_nSINGLE_VEHICLE
 * @brief Define un vehiculo, sin formaci�n mini tren.
 */
#define MINITRAINTAG_nSINGLE_VEHICLE	((uint32)FALSE)

/**
 * @def MINITRAINTAG_nNO_MINITRAIN
 * @brief Define minitren nulo
 */
#define MINITRAINTAG_nNO_MINITRAIN	(0xFFFF)

#endif /* MINITRAINTAG_def_H_ */

