/**
 * @copyright
 * This document is a part of the source code and related artifacts
 * for Modutram Autotrén transportation system
 *
 * http://www.modutram.com
 *
 * Copyright © 2020 Modutram
 *
 * Any use of this source code - including reproduction, modification, distribution, 
 * republication, transmission, re-transmission, modification, or public showing - without the prior 
 * written permission of Modutram is strictly prohibited. 
 *
 * @file    SIS_MSF031_MINITRAINTAG.h
 *
 * @brief   MSF031 -- SIL4 -- Almacenar el identificador de minitren asignado por un SIV-P y mantenerlo hasta que un SIV-P lo sobreescriba.  
 * @note
 *        ______________      ______________      ______________
 *        Juan Aguirre        Luis Gómez          Luis González
 *        Diseñador           Verificador         PM 
 *
 * @version SIS 
 * - Juan Aguirre -- 09/06/2020 -- db36ee8eebc10
 *   - Primera Versión
 *     
 */

#ifndef MINITRAINTAG_H_
#define MINITRAINTAG_H_

/* system headers */
#include "Std_Types.h"

/* own headers */

/*****************************************************************************/
/* helper macros */

/* exported variables */

/* exported functions */
/**
 * @fn          void MINITRAINTAG_vInit(void)
 * @version     ISF147 -- VyShm
 * @brief       Inicializa la memoria estatica del componente 
 * @pre         Ninguna
 * @post        Ninguna
 * @return      void
*/
extern          void MINITRAINTAG_vInit(void);



/**
 * @fn          void MINITRAINTAG_vMonitor(void)
 * @version     ISF148 -- Gk9rX
 * @brief       Obtiene el Tag de mini tren y la prioridad del vehiculo en el mini tren mas recientes enviado por los SIV´s
 * @pre         Previamente debe ejecutarse la interfase #MINITRAINTAG_vInit
 * @post        Ninguna
 * @return      void
*/
extern          void MINITRAINTAG_vMonitor(void);



/**
 * @fn          uint32 MINITRAINTAG_u32GetTag(void)
 * @version     ISF149 -- sZ3Qn
 * @brief       Retorna el Tag de mini tren
 * @pre         Previamente debe ejecutarse la interfase #MINITRAINTAG_vMonitor
 * @post        Ninguna
 * @return      uint32
 *                  - Rango del tipo A = { {x | (x ∈ ℕ) ∩ (x ∈ [0, 2^32-1])}
 *                  - Clases válidas (B ∈ A) | B = {
 *                        - B'={(0, 2^31-1]}
 *                        - B''={#MINITRAINTAG_nSINGLE_VEHICLE} }
 *                  - Clases inválidas C = {
 *                        - ⦰ }
*/
extern          uint32 MINITRAINTAG_u32GetTag(void);


/**
 * @fn          uint16 MINITRAINTAG_u16GetMiniTrnPrio(void)
 * @version     ISF152 -- fC40L
 * @brief       Retorna la prioridad del vehiculo en el minitren
 * @pre         Previamente debe ejecutarse la interfase #MINITRAINTAG_vMonitor
 * @post        Ninguna
 * @return      uint16
 *                  - Rango del tipo A = { {x | (x ∈ ℕ) ∩ (x ∈ [0, 2^16-1])}
 *                  - Clases válidas (B ∈ A) | B = {
 *                        - B'={[0, #MINITRAINTAG_nNO_MINITRAIN)} }
 *                  - Clases inválidas C = {
 *                        - ⦰ }
*/
extern          uint16 MINITRAINTAG_u16GetMiniTrnPrio(void);





#endif /* MINITRAINTAG_H_ */
